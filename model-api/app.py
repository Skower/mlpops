from fastapi import FastAPI, status
from rag_milvus import chain, query_store
from pydantic import BaseModel


# print(chain.invoke("How are you "))

class LLMRequest(BaseModel):
    question: str

class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""
    status: str = "OK"

app = FastAPI()

@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """
    ## Perform a Health Check
    Endpoint to perform a healthcheck on. This endpoint can primarily be used Docker
    to ensure a robust container orchestration and management is in place. Other
    services which rely on proper functioning of the API service will not deploy if this
    endpoint returns any other HTTP status code except 200 (OK).
    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck(status="OK")

@app.post("/chain")
def read_chain(llm_request: LLMRequest):
    query_store.add_texts([llm_request.question])
    return chain.invoke(llm_request.question)

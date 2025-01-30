from fastapi import APIRouter

router = APIRouter(prefix='/status', tags=['status'])


@router.get('/')
async def check_status() -> bool:
    """
    Check service status.
    """

    return True

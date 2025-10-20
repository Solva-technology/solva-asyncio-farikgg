import pytest

from tasks import first_complete


@pytest.mark.asyncio
async def test_first_complete():
    result = await first_complete()
    assert result == 'fast'

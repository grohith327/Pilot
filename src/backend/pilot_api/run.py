import logging
import uvicorn
from dotenv import load_dotenv

load_dotenv()


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
    )
    logger = logging.getLogger()
    return logger


logger = setup_logging()

if __name__ == "__main__":
    uvicorn.run("pilot_api.main:app", host="0.0.0.0", port=8000, reload=True)

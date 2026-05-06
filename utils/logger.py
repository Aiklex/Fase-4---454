# utils/logger.py

import logging

logging.basicConfig(
    filename="eventos.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("software_fj")

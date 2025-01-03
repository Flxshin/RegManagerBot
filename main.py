from app.utils.db_utils import create_tables
from app.bot.bot_manager import run_bot
from config import settings
from app.utils.logger import logger

# 需要安装的模块：无

def init_app():
    """初始化应用"""
    logger.info("初始化应用...")

    # 创建数据库表
    create_tables()
    logger.info("数据库表创建完成")
    logger.info(f"邀请码系统已{'开启' if settings.INVITE_CODE_SYSTEM_ENABLED else '关闭'}")
    logger.info("初始化完成")

if __name__ == "__main__":
    init_app()
    run_bot()
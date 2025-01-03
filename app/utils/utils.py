from app.utils.logger import logger
from telebot.apihelper import ApiTelegramException

# 需要安装的模块：无

def paginate_list(data_list, page_size):
    """
    对列表进行分页

    Args:
        data_list: 要分页的列表
        page_size: 每页的条目数

    Returns:
         一个列表的列表，其中每个内部列表代表一页数据
    """
    logger.debug(f"开始分页列表, pageSize={page_size}, listSize={len(data_list)}")
    if not data_list or page_size <= 0 :
        logger.warning("列表为空或者分页大小不合法")
        return []
    
    paginated_list = []
    # if len(data_list) <= page_size:
    #     paginated_list.append(data_list)
    #     logger.debug(f"无需分页")
    # else:
    for i in range(0, len(data_list), page_size):
        paginated_list.append(data_list[i:i + page_size])
    logger.debug(f"分页列表成功, 总页数={len(paginated_list)}, pageSize={page_size}, listSize={len(data_list)}")
    return paginated_list

def get_username_by_telegram_id(bot, chat_id, telegram_id):
    """
    根据 User ID 获取用户名

    Args:
        chat_id: 群组 ID
        telegram_id: 用户 ID

    Returns:
        Telegram 用户名，如果找不到用户则返回 None
    """
    logger.info(f"根据 Telegram ID 获取用户名: chat_id={chat_id}, telegram_id={telegram_id}")
    try:
        chat_member = bot.get_chat_member(chat_id, telegram_id)
        if chat_member and chat_member.user.username:
            logger.debug(f"获取 Telegram 用户名成功: telegram_id={telegram_id}, username={chat_member.user.username}")
            return chat_member.user.username
        else:
            logger.warning(f"未找到 Telegram 用户: telegram_id={telegram_id}")
            return None
    except ApiTelegramException as e:
        logger.error(f"获取 Telegram 用户名失败: telegram_id={telegram_id}, error={e}")
        return None
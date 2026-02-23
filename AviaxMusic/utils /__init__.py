# Utils package

from .formatters import (
    seconds_to_min,
    check_duration,
    speed_converter,
    get_readable_time,
    format_duration,
    convert_bytes,
)

from .database import (
    add_active_chat,
    remove_active_chat,
    get_active_chats,
    is_active_chat,
    add_active_video_chat,
    remove_active_video_chat,
    is_active_video_chat,
    save_playlist,
    get_playlist,
    remove_playlist,
    get_queue,
    set_loop,
    get_loop,
    set_volume,
    get_volume,
    set_volume_video,
    get_volume_video,
    group_assistant,
    is_served_user,
    get_served_users,
    add_served_user,
    is_saved,
    get_theme,
    set_theme,
    save_filter,
    get_filter,
    delete_filter,
    is_autoend,
    set_autoend,
    get_lang,
    set_lang,
    is_video_allowed,
    video_allowed,
    get_global_volume,
    set_global_volume,
)

from .thumbnails import (
    gen_thumb,
    thumb_init,
    thumb_cleanup,
)

from .exceptions import (
    AssistantErr,
    DownloadError,
    InvalidInput,
    NoVideoFound,
    NoAudioFound,
    SpotifyError,
    TelegramError,
    YouTubeError,
)

from .stream import (
    start_stream,
    stop_stream,
    pause_stream,
    resume_stream,
    skip_stream,
    seek_stream,
    speedup_stream,
    change_stream,
    get_stream,
)

from .cache import (
    cache_file,
    get_cached,
    clear_cache,
    get_cache_size,
)

from .playlist import (
    add_to_playlist,
    remove_from_playlist,
    get_user_playlist,
    clear_user_playlist,
)

# Version
__version__ = "1.0.0"

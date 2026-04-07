from __future__ import annotations

import asyncio
from dataclasses import dataclass

try:
    from aiortc import MediaStreamTrack, RTCPeerConnection
except Exception:  # pragma: no cover - optional runtime import
    MediaStreamTrack = object  # type: ignore[assignment]
    RTCPeerConnection = object  # type: ignore[assignment]


@dataclass(slots=True)
class WebRTCSession:
    pc: RTCPeerConnection
    incoming_audio: asyncio.Queue[bytes]
    outgoing_audio: asyncio.Queue[bytes]


async def create_webrtc_session() -> WebRTCSession:
    if RTCPeerConnection is object:
        raise RuntimeError("aiortc is required for WebRTC mode")
    return WebRTCSession(pc=RTCPeerConnection(), incoming_audio=asyncio.Queue(), outgoing_audio=asyncio.Queue())

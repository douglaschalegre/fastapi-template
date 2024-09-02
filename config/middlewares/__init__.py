"""Criação de lista de middlewares"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .exception import register_exception_collector
from .log import register_log_middleware
from .cors import cors
from .profiler import register_profiling_middleware


def register_middlewares(app: FastAPI):
    """Call all register functions of middlewares"""
    register_log_middleware(app)

    # Don't change the order of the below middlewares!
    app.add_middleware(CORSMiddleware, **cors)  # Always third to last!
    register_exception_collector(app)  # Always second to last!
    register_profiling_middleware(app)  # Always last!

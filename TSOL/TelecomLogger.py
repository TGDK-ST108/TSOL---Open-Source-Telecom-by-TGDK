/*=========================================================================
| TGDK_TelecomLogger Module                                                
| © 2025 Sean Tichenor, TGDK, & OliviaAI. All Rights Reserved.            
| Licensed under TGDK Open Source License (TSOL) - BFE Licensing.         
|========================================================================*/

import logging
from datetime import datetime

class TelecomLogger:
    def __init__(self, logfile="tgdk_telecom.log"):
        self.logfile = logfile

    def log_event(self, message, level="INFO"):
        with open("TGDK_Log.txt", "a") as logfile:
            logfile.write(f"{level}: {message}\n")
            
    def info(self, message):
        self.log("INFO", message)
        
    def error(self, message):
        self.log("ERROR", message)
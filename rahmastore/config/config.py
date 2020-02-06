import os
import arrow


class Config:


    def time(self) :
        utc         = arrow.utcnow()
        local       = utc.to('Asia/Jakarta')
        time        = local.isoformat()
        return time
from app.utils import logger
from app.database import session

class ModelMixin(object):
    
    _session = None
    
    @classmethod
    def set_session(cls, session):
        cls._session = session
    
    def save(self, session = None):
        session = self._session or session
        
        if not session:
            raise logger.error(ValueError, "Session not set!")
        
        session.add(self)
        session.commit()
        return self
    
    def refresh(self, session = None):
        session = self._session or session
        
        if not session:
            raise logger.error(ValueError, "Session not set!")
        
        session.refresh(self)
        return self
    
    def delete(self, session = None):
        session = self._session or session
        
        if not session:
            raise logger.error(ValueError, "Session not set!")
        
        session.delete(self)
        session.commit()
        return self
from jst.structure.objects import JstObject
from jst.utils.kvlm import kvlm_parse, kvlm_serialize


class JstCommit(JstObject):
    fmt=b'commit'

    def deserialize(self, data):
        self.kvlm = kvlm_parse(data)

    def serialize(self):
        return kvlm_serialize(self.kvlm)
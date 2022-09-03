from jst.structure.objects import JstObject


class JstBlob(JstObject):
    fmt=b'blob'

    def serialize(self):
        return self.blobdata

    def deserialize(self, data):
        self.blobdata = data
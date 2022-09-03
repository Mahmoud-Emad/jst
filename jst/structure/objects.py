import collections
import hashlib
import sys
import zlib



class JstObject:

    repo = None

    def __init__(self, repo, data=None):
        self.repo=repo

        if data != None:
            self.deserialize(data)

    def serialize(self):
        """This function MUST be implemented by subclasses.

It must read the object's contents from self.data, a byte string, and do
whatever it takes to convert it into a meaningful representation.  What exactly that means depend on each subclass."""
        raise Exception("Unimplemented!")

    def deserialize(self, data):
        raise Exception("Unimplemented!")


def object_read(repo, sha):
    """Read object object_id from Jst repository repo.  Return a
    JstObject whose exact type depends on the object."""
    from jst.structure.commits import JstCommit
    from jst.structure.blobs import JstBlob

    path = repo.repo_file(repo, "objects", sha[0:2], sha[2:])

    with open (path, "rb") as f:
        raw = zlib.decompress(f.read())

        # Read object type
        x = raw.find(b' ')
        fmt = raw[0:x]

        # Read and validate object size
        y = raw.find(b'\x00', x)
        size = int(raw[x:y].decode("ascii"))
        if size != len(raw)-y-1:
            raise Exception("Malformed object {0}: bad length".format(sha))

        # Pick constructor
        if   fmt==b'commit' : c=JstCommit
        elif fmt==b'tree'   : c=JstTree
        elif fmt==b'tag'    : c=JstTag
        elif fmt==b'blob'   : c=JstBlob
        else:
            raise Exception("Unknown type {0} for object {1}".format(fmt.decode("ascii"), sha))

        # Call constructor and return object
        return c(repo, raw[y+1:])

def object_hash(fd, fmt, repo=None):
    from jst.structure.commits import JstCommit
    from jst.structure.blobs import JstBlob
    data = fd.read()

    # Choose constructor depending on
    # object type found in header.
    if   fmt==b'commit' : obj=JstCommit(repo, data)
    # elif fmt==b'tree'   : obj=JstTree(repo, data)
    # elif fmt==b'tag'    : obj=JstTag(repo, data)
    elif fmt==b'blob'   : obj=JstBlob(repo, data)
    else:
        raise Exception("Unknown type %s!" % fmt)

    return object_write(obj, repo)

def object_find(repo, name, fmt=None, follow=True):
    return name

def obj_cat_file(repo, obj, fmt=None):
    obj = object_read(repo, object_find(repo, obj, fmt=fmt))
    sys.stdout.buffer.write(obj.serialize())

def object_write(obj, actually_write=True):
    # Serialize object data
    data = obj.serialize()
    # Add header
    result = obj.fmt + b' ' + str(len(data)).encode() + b'\x00' + data
    # Compute hash
    sha = hashlib.sha1(result).hexdigest()

    if actually_write:
        # Compute path
        path=obj.repo.repo_file(obj.repo, "objects", sha[0:2], sha[2:], mkdir=actually_write)

        with open(path, 'wb') as f:
            # Compress and write
            f.write(zlib.compress(result))

    return sha

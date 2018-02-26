from os import path


class UnsupportedFileTypeError(Exception):
    """
    File type is unsupported at the moment.
    """
    pass


class NonExistentFileError(Exception):
    """
    File does not exist.
    """
    pass


class NotePackage:
    """
    A package of files, usually representing one topic or lecture.
    """

    def __init__(self):
        """
        Initialize a NotePackage object.
        Contains files in .jpg, .pdf, or .png files.

        @type self: NotePackage
        @rtype: None
        """
        self.documents = []
        self.accepted_types = ['.png', '.pdf', '.jpg']
        self.tags = []

    def add_file(self, filename):
        """
        Add a url of a file to the object.
        Only files of type: pdf, jpg, or png can be added.

        @type self: NotePackage
        @type filename: str (url)
        @rtype: None
        """

        extension = os.path.splitext(filename)[1]
        if extension in self.accepted_types:
            self.documents.append(filename)
        else:
            raise UnsupportedFileTypeError("File type cannot be uploaded")

    def remove_file(self, filename):
        """
        Remove a specific file from this package of notes.

        @type self: NotePackage
        @type filename: str (url)
        @rtype: None
        """

        if filename in self.documents:
            self.documents.remove(filename)
        else:
            raise NonExistentFileError("File does not exist in package")

    def add_tag(self, tag):
        """
        Add a tag to this notes package.

        @type self: NotePackage
        @type tag: tag
        @rtype: None
        """

        # If tag does not exist, create new tag, add it, and add association
        # If tag does exist, add it, and add association
        self.tags.append(tag)

    def remove_tag(self, tag):
        """
        Remove a tag from this notes package.

        @type self: NotePackage
        @type tag: tag
        @rtype: None
        """

        if tag in self.tags: \
                # Remember to remove association
            self.tags.remove(tag)
        else:
            raise Exception("Tag is not part of this package")



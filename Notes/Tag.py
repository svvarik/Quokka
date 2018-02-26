from Notes import NotePackage


class Tag:
    """
    Tags that describe documents.
    """

    def __init__(self, tag_name):
        """
        Initialize a tag object
        """
        self.associated_pkgs = []
        self.name = tag_name

    def add_association(self, notes_package):
        """
         Add an association between this tag and a NotesPackage.

         @type self: Tag
         @type notes_package: NotesPackage
         @rtype: None
        """
        self.associated_pkgs.append(notes_package)

    def remove_association(self, notes_package):
        """
        Remove an association between this tag and a NotesPackage.

        @type self: Tag
        @type notes_package: NotePackage
        @rtype: None
        """
        if notes_package in self.associated_pkgs:
            self.associated_pkgs.remove(notes_package)
        else:
            raise Exception("Not an associated package")

"""
A User on the site.
"""


class User:
    """
    A user on the Quokka Note site.

    === Attributes ===
    username: str
    password: str
    email: str
    is_verified: bool
    courses: list[course]
    notes: list[NotePackage]
    uploaded_notes: int
    """

    def __init__(self, username, password, email):
        """
        Initializes a User object.

        :param username: str
        :param password: str
        :param email: str
        """
        self.username, self.password, self.email = username, password, email
        self.is_verified = False
        self.courses = []
        self.notes = []
        self.uploaded_notes = []

    def verify_user(self):
        """
        Verify a user upon receiving some verification from an email.

        :return: None
        """
        self.is_verified = True

    def add_course(self, course):
        """
        Add a course to this user's list of subscribed courses.

        :param course: Course
        :return: None
        """
        self.courses.append(course)

    def remove_course(self, course):
        """
        Remove a course from this user's list of subscribed courses.

        :param course: Course
        :return: None
        """
        self.courses.remove(course)

    # TODO
    def upload_note_packae(self, package):
        self.notes.append(package)
        self.uploaded_notes += 1
        pass

    #TODO
    def remove_note_package(self, package):
        self.notes.remove(package)
        self.uploaded_notes -= 1
        pass
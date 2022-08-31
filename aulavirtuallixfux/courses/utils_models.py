from pathlib import Path


class UploadToFiles:
    def __init__(self, name):
        self.name = name

    def __call__(self, instance, filename):
        extension = 'file' + Path(filename).suffix
        return '{course_id}/foro/files/{}/{}'.format(instance.course.id,extension,self.name)

    def deconstruct(self):
        return ('courses.utils_models.UploadToFiles', [self.fieldname], {})
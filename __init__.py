from binaryninja.architecture import Architecture
from binaryninja.binaryview import BinaryView
from binaryninja.enums import SegmentFlag

class MyView(BinaryView):
    name = "MyView"
    long_name = "Rebase-Program"

    def __init__(self, data):
        BinaryView.__init__(self, parent_view = data, file_metadata = data.file)

        #Cortex-M vectors should always be Thumb-2
        self.platform= Architecture['thumb2'].standalone_platform

        #Create a new segment, set the base address to 0x37FC0, and read the data file
        self.add_auto_segment(0x37FC0, 0x200000, 0, 0x200000, SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable)

    @classmethod
    def is_valid_for_data(self, data):
        return True

MyView.register()
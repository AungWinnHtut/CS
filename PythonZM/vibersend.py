from viberbot.api.messages import (
    TextMessage,
    ContactMessage,
    PictureMessage,
    VideoMessage
)
from viberbot.api.messages.data_types.contact import Contact

# creation of text message
text_message = TextMessage(text="sample text message!")

# creation of contact message
contact = Contact(name="Viber user", phone_number="0123456789")
contact_message = ContactMessage(contact=contact)

# creation of picture message
picture_message = PictureMessage(text="Check this", media="https://site.com/img.jpg")

# creation of video message
video_message = VideoMessage(media="https://mediaserver.com/video.mp4", size=4324)
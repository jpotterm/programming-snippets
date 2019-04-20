# First, find OBJ_ID
from django.contrib.admin.models import LogEntry
entries = LogEntry.objects.filter(object_id=OBJ_ID)[:3]
entries[0].content_type # <ContentType: Second level page>
ct = entries[0].content_type
entries = LogEntry.objects.filter(content_type=ct, object_id=OBJ_ID)
entry_strings = ['{}\t\t{}\t\t{}'.format(x.action_time.isoformat(), x.user.username, x.change_message.replace('\n', ' ').encode('utf-8')) for x in entries]
print '\n'.join(entry_strings)

from gettext import gettext as _
import random
import time
import string
random.seed(time.time())
N = 32
TEST_DOMAIN =_(''.join(random.choice(string.ascii_uppercase + string.digits) for
                x in range(N)) + ".foo.bar.test_domain.scl3.mozilla.com")
TEST_FQDN = "testfqdn."+TEST_DOMAIN
TEST_IPv4 = "10.1.2.3"
TEST_IPv6 = "1234:1234::1"
TEST_COMMENT = '"This is a comment"'
TEST_TTL = "9999"

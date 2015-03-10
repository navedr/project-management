# Create your views here.
import dropbox

def dropbox_test():
    app_key = 'w4kmbiz4gs1zc06'
    app_secret = 'wvx5m0w8btn4t3a'

    # flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    #
    # authorize_url = flow.start()
    # print '1. Go to: ' + authorize_url
    # print '2. Click "Allow" (you might have to log in first)'
    # print '3. Copy the authorization code.'
    # code = raw_input("Enter the authorization code here: ").strip()
    #
    # access_token, user_id = flow.finish(code)

    client = dropbox.client.DropboxClient('wTKUMukHZb8AAAAAAAADXkYy1JOVg8X3l6vdpQ6Fj7oB0dIST5MS1sePHWcaxKlN')
    # print 'linked account: ', client.account_info()

    # f = open('/Users/rangwaln/Downloads/ABC_Holidays.pdf', 'rb')
    # response = client.put_file('/ABC_Holidays-2015.pdf', f)
    # print 'uploaded: ', response

    # folder_metadata = client.metadata('/')
    # print 'metadata: ', folder_metadata

    f, metadata = client.get_file_and_metadata('/ABC_Holidays-2015.pdf')
    # out = open('/Users/rangwaln/Downloads/ABC_Holidays-2015.pdf', 'wb')
    # out.write(f.read())
    # out.close()
    print 'file metadata: ', metadata

    media = client.media('/ABC_Holidays-2015.pdf')
    print 'media: ', media
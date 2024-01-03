import speedtest


def test_internet_speed():

    """
    A function that tests the internet speed and displays various information.

    Returns:
        None
    """

    # Create a SpeedtestClient object
    st = speedtest.Speedtest()

    # Perform the speed test
    print('Running internet speed test...')
    download_speed = st.download()
    upload_speed = st.upload()
    ping_result = st.results.ping

    # Print the results
    print('================================')
    print('Internet Speed Test Results:')
    print('================================')
    print('Download Speed: {:.2f} Mbps'.format(download_speed / 1000000))
    print('Upload Speed: {:.2f} Mbps'.format(upload_speed / 1000000))
    print('Ping: {:.2f} ms'.format(ping_result))
    print('Server: {}'.format(st.results.server['sponsor']))


if __name__ == "__main__":
    test_internet_speed()

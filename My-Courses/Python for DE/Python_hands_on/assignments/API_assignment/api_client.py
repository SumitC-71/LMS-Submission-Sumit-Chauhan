import requests
from config_logger import get_logger
from requests.exceptions import RequestException, Timeout, ConnectionError

# Example APIs
posts_api = 'https://jsonplaceholder.typicode.com/posts'
users_api = 'https://jsonplaceholder.typicode.com/users'
logger = get_logger()


def fetch_data(api, timeout=3):
    try:
        res = requests.get(api, timeout=timeout)
        
        # Check for non-success status codes
        if res.status_code == 404:
            logger.error(f'Invalid end-point: {api} returned 404 Not Found')
            raise Exception('Invalid end-point: 404 Not Found')
        
        if res.status_code != 200:
            logger.error(f'API returned non-success status code: {res.status_code}')
            raise Exception(f'API Error: Status code {res.status_code}')
        
        logger.info(f'Successfully fetched data from {api}')
        return res
    
    except Timeout as e:
        logger.error(f'Request timeout: Connection timed out after {timeout}s while accessing {api}')
        return None
    except ConnectionError as e:
        logger.error(f'Connection error: Failed to connect to {api}. Details: {str(e)}')
        return None
    except RequestException as e:
        logger.error(f'Request exception: {str(e)} while accessing {api}')
        return None
    except Exception as e:
        logger.error(f'Unexpected error: {str(e)} while accessing {api}')
        return None


# Test the function
# if __name__ == '__main__':
#     result = fetch_data(posts_api)
#     if result:
#         print(f'Status Code: {result.status_code}')
#         print(f'Data fetched successfully')
#     else:
#         print('Failed to fetch data - check api_errors.log')

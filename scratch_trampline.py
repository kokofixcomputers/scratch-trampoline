from flask import Flask, request, jsonify
import requests
from aiohttp import web, ClientSession
import asyncio

async def fetch_data(url, headers=None, cookies=None):
    """Fetch data from a given URL with optional headers and cookies.
    
    Returns a tuple of (data, content_type) where data is the JSON response
    and content_type is the Content-Type header from the response.
    """
    async with ClientSession() as session:
        async with session.get(url, headers=headers, cookies=cookies) as response:
            data = await response.json()
            content_type = response.headers.get('Content-Type')
            return data, content_type, response.status  # Return both data and Content-Type



app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    """Add CORS headers to all responses."""
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response

def get_xtoken_header(request):
    xtoken = request.headers.get('x-token', None)
    if not xtoken:
        header = {}
    else:
        header = {
            'x-token': xtoken
        }
    return header

@app.route('/projects/<int:project_id>', methods=['GET', 'OPTIONS', 'PUT'])
def get_project(project_id):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/projects/{project_id}'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})
    elif request.method == 'PUT':
        """Update project data on Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/projects/{project_id}'
        headers = get_xtoken_header(request)
        response = requests.put(scratch_api_url, headers=headers, json=request.json)
        return (response.text, response.status_code, {'Content-Type': response.headers.get('Content-Type')})

@app.route('/studios/<int:studioid>', methods=['GET', 'OPTIONS'])
def get_studio(studioid):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/studios/{studioid}'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/studios/<int:studioid>/activity', methods=['GET', 'OPTIONS'])
def get_studio_activity(studioid):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        if request.args.get('dateLimit'):
            datelimit = "?dateLimit=" + request.args.get('dateLimit')
        else:
            datelimit = ""
        scratch_api_url = f'https://api.scratch.mit.edu/studios/{studioid}/activity{datelimit}'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/studios/<int:studioid>/comments', methods=['GET', 'OPTIONS'])
def get_studio_comments(studioid):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/studios/{studioid}/comments'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/studios/<int:studioid>/comments/<comment_id>', methods=['GET', 'OPTIONS'])
def get_studio_comment(studioid, comment_id):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/studios/{studioid}/comments/{comment_id}'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/studios/<int:studioid>/comments/<comment_id>/replies', methods=['GET', 'OPTIONS'])
def get_studio_comment_replies(studioid, comment_id):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/studios/{studioid}/comments/{comment_id}/replies'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/studios/<int:studioid>/curators', methods=['GET', 'OPTIONS'])
def get_studio_curators(studioid):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/studios/{studioid}/curators'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/studios/<int:studioid>/managers', methods=['GET', 'OPTIONS'])
def get_studio_managers(studioid):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/studios/{studioid}/managers'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/studios/<int:studioid>/projects', methods=['GET', 'OPTIONS'])
def get_studio_projects(studioid):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/studios/{studioid}/projects'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>', methods=['GET', 'OPTIONS'])
def get_user(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})


@app.route('/users/<string:username>/favorites', methods=['GET', 'OPTIONS'])
def get_user_favorites(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/favorites'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/followers', methods=['GET', 'OPTIONS'])
def get_user_followers(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/followers'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/following', methods=['GET', 'OPTIONS'])
def get_user_following(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/following'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/following/studios/projects', methods=['GET', 'OPTIONS'])
def get_user_following_studio_projects(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/following/studios/projects'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/following/users/activity', methods=['GET', 'OPTIONS'])
def get_user_following_activity(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/following/users/activity'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/following/users/loves', methods=['GET', 'OPTIONS'])
def get_user_following_loves(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/following/users/loves'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/following/users/projects', methods=['GET', 'OPTIONS'])
def get_user_following_projects(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/following/users/loves'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/messages/count', methods=['GET', 'OPTIONS'])
def get_user_message_count(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/messages/count'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/messages', methods=['GET', 'OPTIONS'])
def get_user_messages(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/messages'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/projects', methods=['GET', 'OPTIONS'])
def get_user_projects(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/projects'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/projects/recentlyviewed', methods=['GET', 'OPTIONS'])
def get_user_projects_recentlyviewed(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/projects/recentlyviewed'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/projects/<int:projectid>/studios', methods=['GET', 'OPTIONS'])
def get_project_studios(username, projectid):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/projects/{projectid}/studios'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/users/<string:username>/messages/admin', methods=['GET', 'OPTIONS'])
def get_user_message_admin(username):
    if request.method == 'GET':
        """Fetch project data from Scratch API."""
        scratch_api_url = f'https://api.scratch.mit.edu/users/{username}/messages/admin'
        xtoken = request.headers.get('x-token', None)
        if not xtoken:
            header = {}
        else:
            header = {
                'x-token': xtoken
            }

        # Forward the request to the Scratch API
        response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=header))
        #response = requests.get(scratch_api_url)

        return (response, status_code, {'Content-Type': content_type})

@app.route('/projects/<int:project_id>/loves/user/<string:username>', methods=['GET', 'OPTIONS'])
def get_project_loves(project_id, username):
    """Fetch project data from Scratch API."""
    scratch_api_url = f'https://api.scratch.mit.edu/projects/{project_id}/loves/user/{username}'
    
    # Forward the request to the Scratch API
    response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers={'x-token': request.headers.get('x-token')}))
    #response = requests.get(scratch_api_url)

    return (response, status_code, {'Content-Type': content_type})

@app.route('/projects/<int:project_id>/remixes', methods=['GET', 'OPTIONS'])
def get_project_remixes(project_id):
    """Fetch project data from Scratch API."""
    scratch_api_url = f'https://api.scratch.mit.edu/projects/{project_id}/remixes'
    
    # Forward the request to the Scratch API
    headers = get_xtoken_header(request)
    response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers=headers))
    #response = requests.get(scratch_api_url)

    return (response, status_code, {'Content-Type': content_type})

@app.route('/proxy/comments/project/<int:project_id>', methods=['POST', 'OPTIONS'])
def proxy_comments(project_id):
    """Proxy the request to the Scratch API."""
    scratch_api_url = f'https://api.scratch.mit.edu/proxy/comments/project/{project_id}'
    response = requests.post(scratch_api_url, headers={'x-token': request.headers.get('x-token')}, json=request.json)
    return (response.text, response.status_code, {'Content-Type': response.headers.get('Content-Type')})

@app.route('/projects/<int:project_id>/favorites/user/<string:username>', methods=['GET', 'OPTIONS'])
def get_project_favorites(project_id, username):
    """Fetch project data from Scratch API."""
    scratch_api_url = f'https://api.scratch.mit.edu/projects/{project_id}/favorites/user/{username}'
    
    # Forward the request to the Scratch API
    response, content_type, status_code = asyncio.run(fetch_data(scratch_api_url, headers={'x-token': request.headers.get('x-token')}))
    #response = requests.get(scratch_api_url)

    return (response, status_code, {'Content-Type': content_type})
    
@app.route('/cdn2/get_image/project/<string:image>', methods=['GET', 'OPTIONS'])
def get_image_cdn2(image):
    """Fetch project data from Scratch API."""
    scratch_api_url = f'https://cdn2.scratch.mit.edu/get_image/project/{image}'
    
    # Forward the request to the Scratch API
    response = requests.get(scratch_api_url)
    
    if response.ok:  # Check if the request was successful
        # Create a new response object
        return (response.content, response.status_code, {'Content-Type': response.headers.get('Content-Type')})
    else:
        return jsonify({'error': 'Failed to fetch data'}), response.status_code
    
@app.route('/session', methods=['GET', 'OPTIONS'])
def session():
    """Fetch project data from Scratch API."""
    scratch_api_url = f'https://scratch.mit.edu/session'
    header = {
        'x-requested-with': 'XMLHttpRequest'
    }
    
    # Forward the request to the Scratch API
    response = requests.get(scratch_api_url, headers=header, cookies=request.cookies)
    
    return (response.content, response.status_code, {'Content-Type': response.headers.get('Content-Type')})


if __name__ == '__main__':
    app.run(debug=False)
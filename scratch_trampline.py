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
    app.run(debug=True)
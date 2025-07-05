import json
import requests
from mcp.server.fastmcp import FastMCP
from typing import Any, Literal

mcp = FastMCP(
  name='social-hub-mcp',
  host='127.0.0.1',
  port=5713,
  debug=True
)

# 定义资源
@mcp.resource('github://{username}/repos')
def list_github_repos(username: str = 'yaxingson') -> str:
  response = requests.get(f'https://api.github.com/users/{username}/repos')

  if response.status_code == 200:
    repos = response.json()
    return json.dumps(repos)
  else:
    pass

@mcp.resource('bilibili://{account}/video_manuscripts/{pn}/{ps}')
def list_bilibili_video_manuscripts(
  account: str = '', 
  pn: int = 1, 
  ps: int = 1) -> str:
  url = 'https://member.bilibili.com/arcopen/fn/archive/viewlist'
  response = requests.get(
    url=url,
    params={ 'pn':pn, 'ps':ps, 'status':'all' },
    headers={
      'accept':'',
      'access-token':'',
    }
  )

  if response.status_code == 200:
    result = response.json()
    video_manuscripts = result['data']['list']
    return json.dumps(video_manuscripts)
  else:
    pass

@mcp.resource('tiktok://{account}/videos')
def list_tiktok_videos(account: str = '') -> str:
  url = 'https://open.douyin.com/api/douyin/v1/video/video_list'
  response = requests.get(
    url=url,
    params={ 'cursor':0,'count':10,'open_id':'' },
    headers={
      'access-token':'',
      'content-type':'application/json'
    }
  )

  if response.status_code == 200:
    result = response.json()
    videos = result['data']['list']
    return json.dumps(videos)
  else:
    pass

# 定义LLM提示词
@mcp.prompt
def github_repo_rank(
  language: str, 
  topic: str, 
  by: Literal['star', 'fork']) -> str:
  return f'''

  '''

# 定义工具
@mcp.tool
def get_github_user_info(username: str) -> str:
  '''根据用户名获取Github用户信息'''
  url = f'https://api.github.com/users/{username}'  
  response = requests.get(url)

  if response.status_code == 200:
    return json.dumps(response.json())
  else:
    pass

@mcp.tool
def get_bilibili_video_manuscript_info() -> str:
  '''查询Bilibili平台授权用户的单一视频稿件信息'''
  url = 'https://member.bilibili.com/arcopen/fn/archive/view'
  response = requests.get(
    url=url,
    params={'resource_id':''},
    headers={}
  )

  if response.status_code == 200:
    result = response.json()
    video_manuscript_info = result['data']
    return json.dumps(video_manuscript_info)

@mcp.tool
def get_tiktok_user_public_info() -> str:
  '''获取用户的抖音公开信息，包含昵称和头像'''
  url = 'https://open.douyin.com/oauth/userinfo'

  response = requests.post(
    url=url,
    headers={'content-type':'application/json'},
    data={
      'access_token':'',
      'open_id':''
    }
  )

  if response.status_code == 200:
    result = response.json()
    user_public_info = result['data']
    return json.dumps(user_public_info)

if __name__ == '__main__':
  # mcp.run(transport='stdio')

  requests.get('xxxx')


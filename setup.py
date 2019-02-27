from setuptools import setup

setup(
    name='LikeAndShareTwitterBot',
    author='José Ignacio Amelivia Santiago',
    author_email='jignacio.amelivia@gmail.com',
    url='https://namelivia.com',
    description='This is a small python bot for linking and sharing posts',
    license='LICENSE',
    long_description=open('README.md').read(),
    packages=['like_and_share_twitter_bot'],
    include_package_data=True,
    install_requires=[
        'python-twitter >= 3.5',
    ],
)

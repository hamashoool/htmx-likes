from django.shortcuts import render

from likes.models import Post, Like


def posts(request):
    context = {}

    posts = Post.objects.all()
    context['posts'] = posts

    return render(request, 'likes/posts.html', context)


def like(request, post_id):
    post = Post.objects.get(id=post_id)
    try:
        like = Like.objects.get(post=post)
        like.likes += 1
        like.save()
    except Exception as e:
        Like.objects.create(post=post, likes=1)

    return render(request, 'likes/like_section.html', {'post': post})


def dislike(request, post_id):
    post = Post.objects.get(id=post_id)
    try:
        like = Like.objects.get(post=post)
        like.likes -= 1
        like.save()
    except Exception as e:
        pass

    return render(request, 'likes/like_section.html', {'post': post})

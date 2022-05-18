from rest_framework import generics

from api.v1.books import mixins


class BookListAPIView(mixins.BookAPIViewMixin, generics.ListAPIView):
    """ Список книги """
    pass


class BookCreateAPIView(mixins.BookAPIViewMixin, generics.CreateAPIView):
    """ Создать книгу """
    pass


class BookUpdateAPIView(mixins.BookAPIViewMixin, generics.UpdateAPIView):
    """ Редактировать книгу """
    pass


class BookDetailAPIView(mixins.BookAPIViewMixin, generics.RetrieveAPIView):
    """ О книге подробно """
    pass


class BookDeleteAPIView(mixins.BookAPIViewMixin, generics.DestroyAPIView):
    """ Удалить книгу """
    pass

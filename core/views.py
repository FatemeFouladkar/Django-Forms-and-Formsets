from django.views.generic import CreateView
from django.db import transaction

from .models import Author
from .forms import AuthorForm, BookFormSet


class CreateAuthorView(CreateView):
    template_name = 'core/create_author.html'
    model = Author
    form_class = AuthorForm
    success_url = './'

    def get_context_data(self, **kwargs):
        context = super(CreateAuthorView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = BookFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = BookFormSet(instance=self.object)
        return context

 
    def form_valid(self, form, formset):
        with transaction.atomic():
            self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)
        

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = BookFormSet(self.request.POST, self.request.FILES)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_invalid(self, form, formset):
        return self.render_to_response(
                self.get_context_data(form=form,
                                    formset=formset))
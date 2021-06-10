from django.views.generic import ListViewfrom ..models import PythonTipTEMPLATE_URL = 'apps/twee'class HomePage(ListView):    model = PythonTip    template_name = f'{TEMPLATE_URL}/home.html'    paginate_by = '12'    def get_queryset(self):        qs = super().get_queryset()        if self.request.GET.get('filter_by') == 'like':            return qs.filter(likes__gt=0)        if self.request.GET.get('filter_by') == 'unlike':            return qs.filter(likes__lt=1)        if self.request.GET.get('filter_by') == 'retweet':            return qs.filter(retweets__gt=0)        if self.request.GET.get('filter_by') == 'n_retweet':            return qs.filter(retweets=0)        return qs    def get_ordering(self):        ordering = super().get_ordering()        if self.request.GET.get('sort') == 'newest':            ordering = ['-timestamp']        if self.request.GET.get('sort') == 'oldest':            ordering = ['timestamp']        if self.request.GET.get('sort') == 'likes_asc':            ordering = ['likes']        if self.request.GET.get('sort') == 'likes_desc':            ordering = ['-likes']        if self.request.GET.get('sort') == 'retweets_asc':            ordering = ['retweets']        if self.request.GET.get('sort') == 'retweets_desc':            ordering = ['-retweets']        if self.request.GET.get('sort') == 'link':            ordering = ['links']        if self.request.GET.get('sort') == 'no_link':            ordering = ['-links']        if self.request.GET.get('sort') == 'hash':            ordering = ['-hash_tags']        if self.request.GET.get('sort') == 'no_hash':            ordering = ['hash_tags']        return ordering
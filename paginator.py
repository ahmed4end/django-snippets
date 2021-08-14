from django.core.paginator import Paginator

paginator.count
paginator.num_pages
paginator.page_range
paginator.page(2)

page = paginator.page(2)

page.has_next()	
page.has_previous()
page.has_other_pages()	
page.next_page_number()	
page.previous_page_number()	
page.start_index()		
page.end_index()		



# views.py function ex
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'core/user_list.html', { 'users': users })

# views class based ex
class UserListView(ListView):
    model = User
    template_name = 'core/user_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'users'  # Default: object_list
    paginate_by = 10
    queryset = User.objects.all()  # Default: Model.objects.all()


# index.html 
<table class="table table-bordered">
  <thead>
    <tr>
      <th>Username</th>
      <th>First name</th>
      <th>Email</th>
    </tr>
  </thead>
  <tbody>
    {% for user in users %}
      <tr>
        <td>{{ user.username }}</td>
        <td>{{ user.first_name }}</td>
        <td>{{ user.email }}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>

{% if users.has_other_pages %}
  <ul class="pagination">
    {% if users.has_previous %}
      <li><a href="?page={{ users.previous_page_number }}">&laquo;</a></li>
    {% else %}
      <li class="disabled"><span>&laquo;</span></li>
    {% endif %}
    {% for i in users.paginator.page_range %}
      {% if users.number == i %}
        <li class="active"><span>{{ i }} <span class="sr-only">(current)</span></span></li>
      {% else %}
        <li><a href="?page={{ i }}">{{ i }}</a></li>
      {% endif %}
    {% endfor %}
    {% if users.has_next %}
      <li><a href="?page={{ users.next_page_number }}">&raquo;</a></li>
    {% else %}
      <li class="disabled"><span>&raquo;</span></li>
    {% endif %}
  </ul>
{% endif %}
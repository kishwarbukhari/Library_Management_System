from django.contrib.auth.decorators import login_required, user_passes_test


def librarian_required(view_fun):
    decorated_view_fun = login_required(
        user_passes_test(lambda u: u.is_librarian)(view_fun)

    )
    
    return decorated_view_fun

def student_required(view_fun):
    decorated_view_fun = login_required(
        user_passes_test(lambda u: u.is_student)(view_fun)

    )
    
    return decorated_view_fun
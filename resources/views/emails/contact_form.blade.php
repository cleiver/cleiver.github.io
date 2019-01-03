@component('mail::message')
# Contato pelo Formulário

Mensagem de {{ $form['name'] }} ({{ $form['email'] }}):

@component('mail::panel')
{{ $form['message'] }}
@endcomponent

@endcomponent

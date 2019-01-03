<?php
namespace App\Http\Controllers;

use App\Mail\ContactForm;
use App\Http\Requests\ReCaptchataFormRequest;
use Illuminate\Support\Facades\Mail;
use Symfony\Component\HttpFoundation\Request;

class ContactController extends Controller
{
    public function send(ReCaptchataFormRequest $request)
    {
        Mail::to('cleiver@gmail.com')->send(new ContactForm($request->validated()));

        $encoded = json_encode(['message' => 'Your message was sent. I will answer it as soon as I read it :D']);
        header('Content-Type: application/json');
        print($encoded);
    }
}
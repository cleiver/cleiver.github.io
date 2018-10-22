<?php
namespace App\Http\Controllers;

use App\Http\Controllers\Controller;

class ResumeController extends Controller
{
    public function home()
    {
        return view('layouts.master');
    }
}
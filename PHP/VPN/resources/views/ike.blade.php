<!doctype html>
<html lang="{{ app()->getLocale() }}">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>IKE builder</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Raleway:100,600" rel="stylesheet" type="text/css">

        <!-- Styles -->

    </head>
    <body>
        <div class="flex-center position-ref full-height">

            <div class="content">
                <div class="title m-b-md">
                    <h1>IKE builder</h1>
                </div>


                <div>
                    <h2>IKE proposal</h2>
                    {!! Form::open(['url' => 'foo/bar']) !!}
                        <label>Name:</label>
                        {!! Form::text('name') !!}
                        <br>
                        <label>Authentication algorithm:</label>
                        {!! Form::select('auth_algo', ['md5' => 'md5', 'sha-256' => 'sha-256', 'sha-384' => 'sha-384', 'sha1' => 'sha1']); !!}

                    {!! Form::close() !!}

                </div>

                <div class="links">
                    <a href="/ike">IKE builder</a>
                    <a href="/ipsec">IPsec builder</a>
                </div>
            </div>
        </div>
    </body>
</html>

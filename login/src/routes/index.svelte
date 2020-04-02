<script>
  let email = "";
  let password = "";
  let isLoading = false;
  let isSuccess = false;
  const submit = () => new Promise(resolve => setTimeout(resolve, 1000))
  let errors = {};
  const handleSubmit = () => {
    errors = {};
    if (email.length === 0) {
      errors.email = "Field should not be empty";
    }
    if (password.length === 0) {
      errors.password = "Field should not be empty";
    }
    if (Object.keys(errors).length === 0) {
      isLoading = true;
      submit({ email, password })
        .then(() => {
          isSuccess = true;
          isLoading = false;
        })
        .catch(err => {
          errors.server = err;
          isLoading = false;
        });
    }
  };
</script>

<style>

div.my-login-page {
	background-color: #f7f9fb;
	font-size: 14px;
    position: absolute;
	height: 100%;
	width: 100%;
}

.my-login-page .brand {
	width: 90px;
	height: 90px;
	overflow: hidden;
	border-radius: 50%;
	margin: 40px auto;
	box-shadow: 0 4px 8px rgba(0,0,0,.05);
	position: relative;
	z-index: 1;
}

.my-login-page .brand img {
	width: 100%;
}

.my-login-page .card-wrapper {
	width: 400px;
}

.my-login-page .card {
	border-color: transparent;
	box-shadow: 0 4px 8px rgba(0,0,0,.05);
}

.my-login-page .card.fat {
	padding: 10px;
}

.my-login-page .card .card-title {
	margin-bottom: 30px;
}

.my-login-page .form-control {
	border-width: 2.3px;
}

.my-login-page .form-group label {
	width: 100%;
}

.my-login-page .btn.btn-block {
	padding: 12px 10px;
}

.my-login-page .footer {
	margin: 40px 0;
	color: #888;
	text-align: center;
}

@media screen and (max-width: 425px) {
	.my-login-page .card-wrapper {
		width: 90%;
		margin: 0 auto;
	}
}

@media screen and (max-width: 320px) {
	.my-login-page .card.fat {
		padding: 0;
	}

	.my-login-page .card.fat .card-body {
		padding: 15px;
	}
}
</style>


<div class="my-login-page">
	<section class="h-100">
		<div class="container h-100">
			<div class="row justify-content-md-center h-100">
				<div class="card-wrapper">
					<div class="brand">
						<img src="great-success.png" alt="logo">
					</div>
					<div class="card fat">
						<div class="card-body">
							<h4 class="card-title">Login</h4>
							<form class="my-login-validation" on:submit|preventDefault={handleSubmit}>
								<div class="form-group">
									<label for="email">E-Mail Address</label>
									<input id="email" type="email" class="form-control" name="email" bind:value={email} required autofocus>
									<div class="invalid-feedback">
										Email is invalid
									</div>
								</div>

								<div class="form-group">
									<label for="password">Password
										<a href="forgot.html" class="float-right">
											Forgot Password?
										</a>
									</label>
									<input id="password" type="password" class="form-control" name="password" required bind:value={password}>
								    <div class="invalid-feedback">
								    	Password is required
							    	</div>
								</div>

								<div class="form-group">
									<div class="custom-checkbox custom-control">
										<input type="checkbox" name="remember" id="remember" class="custom-control-input">
										<label for="remember" class="custom-control-label">Remember Me</label>
									</div>
								</div>

								<div class="form-group m-0">
									<button type="submit" class="btn btn-primary btn-block" disabled={isLoading}>
										Login
									</button>
								</div>
								<div class="mt-4 text-center">
									Don't have an account? <a href="register.html">Create One</a>
								</div>
							</form>
						</div>
					</div>
					<div class="footer">
						Copyright &copy; 2020 &mdash; Your Company 
					</div>
				</div>
			</div>
		</div>
	</section>
</div>
Vue.config.keyCodes.atsign = 50;

var a = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data() {
        return {
            show1: false,
            show2: false,
            show3: false,
            image: '',
            alert: true,
            form: {
                fname: '',
                lname: '',
                email: '',
                username: '',
                password: '',
                cpassword: '',
                age: '',
                gender: '',
                loginusername: '',
                loginpassword: '',
                test: '',
            },
            auth_modal: false,
            loginpage: true,
            loginvalid: false,
            title: 'MinuteTalk',
            login_error: '',
            signup_error: '',
            firstnameRules: [
                v => this.is_valid_field(v) || 'First Name is required'
            ],
            lastnameRules: [
                v => this.is_valid_field(v) || 'Last Name is required'
            ],
            usernameRules: [
                v => this.is_valid_field(v) || 'Username is required'
            ],
            passwordRules: [
                v => this.is_valid_field(v) || 'Password is required',
                v => this.is_valid_password(v) || 'Password must be or more than 8 characters'
            ],
            emailRules: [
                v => this.is_valid_email(v) || 'E-mail must be valid'
            ],
            confirmRules: [
                v => (this.is_valid_password2(v) && this.is_valid_password(password)) || 'Passwords do not match'
            ],
            ageRules: [
                v => this.is_valid_field(v) || 'Age is required',
                v => this.is_valid_age(v) || 'You must be 18 years old'
            ],
        }
    },
    methods: {
        onFileChange(e) {
            var files = e.target.files || e.dataTransfer.files;
            if (!files.length)
                return;
            this.createImage(files[0]);
        },
        createImage(file) {
            var image = new Image();
            var reader = new FileReader();
            var vm = this;

            reader.onload = (e) => {
                vm.image = e.target.result;
            };
            reader.readAsDataURL(file);
        },
        removeImage: function(e) {
            this.image = '';
        },
        login: function() {
            $.ajax({
                url: 'minutetalk/login',
                type: 'POST',
                data: {
                    username: this.form.loginusername,
                    password: this.form.loginpassword,
                    csrfmiddlewaretoken: this.$refs.login_form.csrfmiddlewaretoken.value
                },
                success: response => {
                    if (response['error']) {
                        this.auth_modal = true
                        this.login_error = response['error']
                        this.form.loginusername = ''
                        this.form.loginpassword = ''
                    } else {
                        window.location.href = "minutetalk/home"
                    }
                }
            })
            this.reset()
        },
        signup: function() {
            $.ajax({
                url: 'minutetalk/signup',
                type: 'POST',
                data: {
                    first_name: this.form.fname,
                    last_name: this.form.lname,
                    email: this.form.email,
                    username: this.form.username,
                    password1: this.form.password,
                    age: this.form.age,
                    gender: this.form.gender,
                    csrfmiddlewaretoken: this.$refs.signup_form.csrfmiddlewaretoken.value
                },
                success: response => {
                    if (response['error']) {
                        this.auth_modal = true
                        this.loginpage = false
                        this.signup_error = response['error']
                    } else {
                        console.log("REDIRECTING")
                        window.location.href = "minutetalk/home"
                    }
                }
            })
            this.reset()
        },
        is_valid_field: function(v) {
            return !!v
        },
        is_valid_password: function(v) {
            return v && v.length >= 8
        },
        is_valid_password2: function(v) {
            return v == this.form.password
        },
        is_valid_email: function(v) {
            return /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v)
        },
        is_valid_age: function(v) {
            return (/^\d{1,2}$/ && v >= 18)
        },
        reset: function() {
            this.form.fname = ''
            this.form.lname = ''
            this.form.email = ''
            this.form.username = ''
            this.form.password = ''
            this.form.cpassword = ''
            this.form.age = ''
            this.form.gender = ''
            this.form.loginusername = ''
            this.form.loginpassword = ''
            this.login_error = ''
            this.signup_error = ''
        }
    },

    computed: {
        invalidLogin() {
            return !this.form.loginusername || !this.form.loginpassword;
        },
        invalidSignup() {
                fname = this.form.fname,
                lname = this.form.lname,
                email = this.form.email,
                username = this.form.username,
                password = this.form.password,
                password2 = this.form.cpassword,
                age = this.form.age,
                gender = this.form.gender
            return !fname || !lname || !email || !username || !password || !cpassword || !age || !gender ||
                !this.is_valid_password(password) || !this.is_valid_password2(password2) || !this.is_valid_email(email) ||
                !this.is_valid_age(age);
        }
    }
})
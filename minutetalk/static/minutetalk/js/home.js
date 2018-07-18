var vue = new Vue({
    delimiters: ['[[', ']]'],
    el: '#home',
    data() {
        return {
            dialog: false,
            changepassword: false,
            editprofile: false,
            isEditing: false,
            drawer: null,
            menupopout: false,
            channel_search: '',
            channel_result: [],
            user_search: '',
            user_result: [],
            show_channel_result: false,
            queryHTML: null,
            editformpass: '',
            enterpass: false,
            success: false,
            errorpassword: true,
            validsave: true,
            validedit: false,
            genderchoice: 'All',
            gender: ['All', 'Male', 'Female'],
            agechoice: 'All',
            age: ['All', '18-24', '25-34', '35-44', '45-54', '55-64', '65+'],
            show: true,
            image: '',
            form: {
                fname: '',
                lname: '',
                email: '',
                username: '',
                age: '',
                gender: '',
                test: '',
            },
            editError: '',
            currentpass: '',
            password_match: false,
            changepass: {
                newpassword: '',
                confirmpassword: ''
            },
            users : [],
            channel: {
                show_favorite: false,
                fav: false
            },
            caller: {},
            callee: {},
            incomingcall: false,
            calling: false,
            calleebusy: false,
            calleereject: false,
            name: '',
            details: '',
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
                v => (this.is_valid_password2(v) && this.is_valid_password(v)) || 'Passwords do not match'
            ],
            ageRules: [
                v => this.is_valid_field(v) || 'Age is required',
                v => this.is_valid_age(v) || 'You must be 18 years old'
            ],
            passwordMatchRules: [
                v => this.password_match || 'Incorrect Password'
            ],

            iconlist: [{
                    title: 'Edit Profile',
                    icon: 'person'
                },
                {
                    title: 'Change Password',
                    icon: 'lock'
                },
                {
                    title: 'Logout',
                    icon: 'exit_to_app'
                }
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
            vue.isEditing = true;
            this.image = '';
        },
        dropdown: function(option) {
            if (option == "Edit Profile") {
                this.editprofile = true;
            } else if (option == "Change Password") {
                console.log("Change password")
                this.changepassword = true;
            } else if (option == "Logout") {
                window.location.href = "logout"

            }
        },
        favorite: function(channel_id) {
            this.channel.fav = !this.channel.fav
            this.channel.show_favorite = !this.channel.show_favorite;

            var element = document.getElementById(channel_id.toString());

            if (!this.channel.fav && element) {
                element.parentNode.removeChild(element);
                this.channel.show_favorite = false;
            }

            $.ajax({
                url: '/ajax/add_to_favorite',
                data: {
                    'channel_id': channel_id,
                },
                success: function(data) {
                    if (data['message']) {
                        console.log(data['message'])
                    }
                }
            });
        },
        is_valid_field: function(v) {
            return !!v
        },
        is_valid_password: function(v) {
            return v && v.length >= 8
        },
        is_valid_password2: function(v) {
            return v == this.changepass.newpassword && v.length >= 8
        },
        is_valid_email: function(v) {
            return /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v)
        },
        is_valid_age: function(v) {
            return (/^\d{1,2}$/ && v >= 18)
        },
        edit: function() {
            fname1 = this.form.fname;
            lname1 = this.form.lname;
            email1 = this.form.email;
            username1 = this.form.username;
            age1 = this.form.age;
            gender1 = this.form.gender;
            init();
            // save changes to database
            $.ajax({
                url: 'edit_profile',
                type: 'POST',
                data: {
                    img_src: this.$refs.img_src.src,
                    first_name: this.form.fname,
                    last_name: this.form.lname,
                    email: this.form.email,
                    username: this.form.username,
                    password1: this.editformpass,
                    password2: this.editformpass,
                    age: this.form.age,
                    gender: this.form.gender,
                    csrfmiddlewaretoken: this.$refs.editForm.csrfmiddlewaretoken.value
                },
                success: response => {
                    if (response['error']) {
                        this.editError = response['error']
                    } else {
                        this.success = true
                        this.enterpass = false
                        setTimeout(function(){
                            vue.success = false
                        }, 1 * 1000); // Hide after 1 sec
                        window.location.reload(true);
                    }
                }
            });
            this.editformpass = ""
        },
        edit_pass: function() {
            $.ajax({
                url: 'edit_pass',
                type: 'POST',
                data: {
                    currentpass: this.currentpass,
                    password1: this.changepass.newpassword,
                    password2: this.changepass.confirmpassword,
                    csrfmiddlewaretoken: this.$refs.changePassword.csrfmiddlewaretoken.value
                },
                success: response => {
                    this.success = true
                    setTimeout(function(){
                        vue.success = false
                        }, 1 * 1000); // Hide after 1 sec
                }
            });
            this.reset()
        },
        reset: function() {
            this.isEditing = false;
            this.editprofile = false;
            this.changepassword = false;
            this.changepass.currentpass = ''
            this.changepass.newpassword = ''
            this.changepass.confirmpassword = ''
            this.$refs.changePassword.reset();
        },
        createSession: function(caller_id){
            $.ajax({
                async:false,
                url: 'ajax/session',
                data: {
                },
                success: response => {
                    console.log(response)
                    sendSession(response['session'],caller_id)
                }
            })
        },
        startCall: function(session_id){
            console.log('Starting call....')
            $.ajax({
                async:false,
                url: 'ajax/token',
                data: {
                    'session_id': session_id
                },
                success: response => {
                    window.location.href += '/videochat'
                }
            })
        },
        talk: function(id, first_name, last_name, img_src){
            this.calling = true
            var callee = {
                'id': id,
                'name': first_name + ' ' + last_name,
                'img_src': img_src
            }
            this.callee = callee
            talk(id)
            console.log('talk')
        },
        cancel_call: function(id){
            this.calling = false
            cancel_call(id)
        },
        decline_call: function(id){
            decline_call(id)

        }
    },
    watch: {
        channel_search: function() {
            var res = []
            if (this.channel_search.trim()) {
                $.ajax({
                    async: false,
                    url: 'ajax/search_channel',
                    data: {
                        'query': this.channel_search,
                    },
                    success: function(data) {
                        if (data.titles.length > 0) {
                            res = data.titles;
                        }
                    }
                });
                this.channel_result = res

            }
        },
        user_search: function() {
            var channel_id = parseInt(window.location.pathname.substring(1))
            this.user_result = filterUser(channel_id, this.user_search, this.agechoice, this.genderchoice)
        },
        agechoice: function() {
            var channel_id = parseInt(window.location.pathname.substring(1))
            this.user_result = filterUser(channel_id, this.user_search, this.agechoice, this.genderchoice)
        },
        genderchoice: function() {
            var channel_id = parseInt(window.location.pathname.substring(1))
            this.user_result = filterUser(channel_id, this.user_search, this.agechoice, this.genderchoice)
        },
        currentpass: function(){
            var value = false;
            $.ajax({
                    async: false,
                    url: 'ajax/check_password',
                    data: {
                        'password': this.currentpass,
                    },
                    success: function(data) {
                        value = data['password_match']
                    }
                });
            this.password_match=  value
        }
    },
    computed: {
        channel_search_result() {
            return this.channel_result;
        },
        user_search_result() {
            return this.user_result;
        },
        valid_prof_form() {
            fname = this.form.fname;
            lname = this.form.lname;
            email = this.form.email;
            username = this.form.username;
            age = this.form.age;
            gender = this.form.gender;
            return !this.isEditing || (this.isEditing && (!fname || !lname || !email || !username || !age || !gender ||
                !this.is_valid_email(email) || !this.is_valid_age(age) ));
        },
        valid_pass_form(){
            new_pass = this.changepass.newpassword
            conf_pass = this.changepass.confirmpassword
            return !this.password_match ||  !this.is_valid_password(new_pass) || !this.is_valid_password2(conf_pass)
        }
    }
});






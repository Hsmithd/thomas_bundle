# Play: Alpha - setup

- hosts: loadbalancers
  become: true
  vars:
    app_name: "alpha_app"
    retry_count: 1

  tasks:
    - name: Ensure lemon-task-1 is present
      ansible.builtin.file:
        path: /opt/alpha/lemon-task-1
        state: directory

    - name: Template lemon-task-1 config
      ansible.builtin.template:
        src: templates/lemon-task-1.j2
        dest: /etc/alpha/lemon-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure hotel-task-2 is present
      ansible.builtin.file:
        path: /opt/alpha/hotel-task-2
        state: directory

    - name: Template hotel-task-2 config
      ansible.builtin.template:
        src: templates/hotel-task-2.j2
        dest: /etc/alpha/hotel-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart alpha service
      ansible.builtin.service:
        name: alpha
        state: restarted

## Notes

Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:44Z

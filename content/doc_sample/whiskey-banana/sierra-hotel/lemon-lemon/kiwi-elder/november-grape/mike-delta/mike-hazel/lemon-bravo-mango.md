# Play: Lemon - setup

- hosts: webservers
  become: false
  vars:
    app_name: "lemon_app"
    retry_count: 1

  tasks:
    - name: Ensure papa-task-1 is present
      ansible.builtin.file:
        path: /opt/lemon/papa-task-1
        state: directory

    - name: Template papa-task-1 config
      ansible.builtin.template:
        src: templates/papa-task-1.j2
        dest: /etc/lemon/papa-task-1.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure lemon-task-2 is present
      ansible.builtin.file:
        path: /opt/lemon/lemon-task-2
        state: directory

    - name: Template lemon-task-2 config
      ansible.builtin.template:
        src: templates/lemon-task-2.j2
        dest: /etc/lemon/lemon-task-2.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart lemon service
      ansible.builtin.service:
        name: lemon
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:43Z

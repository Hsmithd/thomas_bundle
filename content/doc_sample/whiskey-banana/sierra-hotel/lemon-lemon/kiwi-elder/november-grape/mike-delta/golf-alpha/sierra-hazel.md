# Play: Sierra - setup

- hosts: all
  become: false
  vars:
    app_name: "sierra_app"
    retry_count: 3

  tasks:
    - name: Ensure echo-task-1 is present
      ansible.builtin.file:
        path: /opt/sierra/echo-task-1
        state: directory

    - name: Template echo-task-1 config
      ansible.builtin.template:
        src: templates/echo-task-1.j2
        dest: /etc/sierra/echo-task-1.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure cherry-task-2 is present
      ansible.builtin.file:
        path: /opt/sierra/cherry-task-2
        state: directory

    - name: Template cherry-task-2 config
      ansible.builtin.template:
        src: templates/cherry-task-2.j2
        dest: /etc/sierra/cherry-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart sierra service
      ansible.builtin.service:
        name: sierra
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:44Z

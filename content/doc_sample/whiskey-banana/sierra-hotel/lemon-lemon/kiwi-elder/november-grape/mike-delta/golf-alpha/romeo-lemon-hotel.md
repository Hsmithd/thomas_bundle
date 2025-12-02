# Play: Romeo - setup

- hosts: webservers
  become: true
  vars:
    app_name: "romeo_app"
    retry_count: 2

  tasks:
    - name: Ensure quebec-task-1 is present
      ansible.builtin.file:
        path: /opt/romeo/quebec-task-1
        state: directory

    - name: Template quebec-task-1 config
      ansible.builtin.template:
        src: templates/quebec-task-1.j2
        dest: /etc/romeo/quebec-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure cherry-task-2 is present
      ansible.builtin.file:
        path: /opt/romeo/cherry-task-2
        state: directory

    - name: Template cherry-task-2 config
      ansible.builtin.template:
        src: templates/cherry-task-2.j2
        dest: /etc/romeo/cherry-task-2.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure november-task-3 is present
      ansible.builtin.file:
        path: /opt/romeo/november-task-3
        state: directory

    - name: Template november-task-3 config
      ansible.builtin.template:
        src: templates/november-task-3.j2
        dest: /etc/romeo/november-task-3.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart romeo service
      ansible.builtin.service:
        name: romeo
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:44Z

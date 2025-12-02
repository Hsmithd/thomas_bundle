# Play: Cherry - setup

- hosts: webservers
  become: true
  vars:
    app_name: "cherry_app"
    retry_count: 4

  tasks:
    - name: Ensure kiwi-task-1 is present
      ansible.builtin.file:
        path: /opt/cherry/kiwi-task-1
        state: directory

    - name: Template kiwi-task-1 config
      ansible.builtin.template:
        src: templates/kiwi-task-1.j2
        dest: /etc/cherry/kiwi-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure quebec-task-2 is present
      ansible.builtin.file:
        path: /opt/cherry/quebec-task-2
        state: directory

    - name: Template quebec-task-2 config
      ansible.builtin.template:
        src: templates/quebec-task-2.j2
        dest: /etc/cherry/quebec-task-2.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart cherry service
      ansible.builtin.service:
        name: cherry
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

***
Generated: 2025-11-07T18:27:44Z

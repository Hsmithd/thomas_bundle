# Play: Sierra - setup

- hosts: db
  become: false
  vars:
    app_name: "sierra_app"
    retry_count: 4

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
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure papa-task-2 is present
      ansible.builtin.file:
        path: /opt/sierra/papa-task-2
        state: directory

    - name: Template papa-task-2 config
      ansible.builtin.template:
        src: templates/papa-task-2.j2
        dest: /etc/sierra/papa-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure juliet-task-3 is present
      ansible.builtin.file:
        path: /opt/sierra/juliet-task-3
        state: directory

    - name: Template juliet-task-3 config
      ansible.builtin.template:
        src: templates/juliet-task-3.j2
        dest: /etc/sierra/juliet-task-3.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure hazel-task-4 is present
      ansible.builtin.file:
        path: /opt/sierra/hazel-task-4
        state: directory

    - name: Template hazel-task-4 config
      ansible.builtin.template:
        src: templates/hazel-task-4.j2
        dest: /etc/sierra/hazel-task-4.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart sierra service
      ansible.builtin.service:
        name: sierra
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:44Z

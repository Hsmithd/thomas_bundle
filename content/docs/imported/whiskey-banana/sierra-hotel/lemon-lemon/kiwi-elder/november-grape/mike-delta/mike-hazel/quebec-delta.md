# Play: Quebec - setup

- hosts: webservers
  become: false
  vars:
    app_name: "quebec_app"
    retry_count: 2

  tasks:
    - name: Ensure grape-task-1 is present
      ansible.builtin.file:
        path: /opt/quebec/grape-task-1
        state: directory

    - name: Template grape-task-1 config
      ansible.builtin.template:
        src: templates/grape-task-1.j2
        dest: /etc/quebec/grape-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure golf-task-2 is present
      ansible.builtin.file:
        path: /opt/quebec/golf-task-2
        state: directory

    - name: Template golf-task-2 config
      ansible.builtin.template:
        src: templates/golf-task-2.j2
        dest: /etc/quebec/golf-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure fig-task-3 is present
      ansible.builtin.file:
        path: /opt/quebec/fig-task-3
        state: directory

    - name: Template fig-task-3 config
      ansible.builtin.template:
        src: templates/fig-task-3.j2
        dest: /etc/quebec/fig-task-3.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart quebec service
      ansible.builtin.service:
        name: quebec
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:43Z

# Play: Kiwi - setup

- hosts: webservers
  become: false
  vars:
    app_name: "kiwi_app"
    retry_count: 3

  tasks:
    - name: Ensure quebec-task-1 is present
      ansible.builtin.file:
        path: /opt/kiwi/quebec-task-1
        state: directory

    - name: Template quebec-task-1 config
      ansible.builtin.template:
        src: templates/quebec-task-1.j2
        dest: /etc/kiwi/quebec-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure cherry-task-2 is present
      ansible.builtin.file:
        path: /opt/kiwi/cherry-task-2
        state: directory

    - name: Template cherry-task-2 config
      ansible.builtin.template:
        src: templates/cherry-task-2.j2
        dest: /etc/kiwi/cherry-task-2.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure date-task-3 is present
      ansible.builtin.file:
        path: /opt/kiwi/date-task-3
        state: directory

    - name: Template date-task-3 config
      ansible.builtin.template:
        src: templates/date-task-3.j2
        dest: /etc/kiwi/date-task-3.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

  handlers:
    - name: restart kiwi service
      ansible.builtin.service:
        name: kiwi
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:45Z

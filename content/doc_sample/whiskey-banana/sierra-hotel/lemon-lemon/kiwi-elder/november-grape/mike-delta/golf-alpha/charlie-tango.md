# Play: Charlie - setup

- hosts: db
  become: false
  vars:
    app_name: "charlie_app"
    retry_count: 2

  tasks:
    - name: Ensure golf-task-1 is present
      ansible.builtin.file:
        path: /opt/charlie/golf-task-1
        state: directory

    - name: Template golf-task-1 config
      ansible.builtin.template:
        src: templates/golf-task-1.j2
        dest: /etc/charlie/golf-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure oscar-task-2 is present
      ansible.builtin.file:
        path: /opt/charlie/oscar-task-2
        state: directory

    - name: Template oscar-task-2 config
      ansible.builtin.template:
        src: templates/oscar-task-2.j2
        dest: /etc/charlie/oscar-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart charlie service
      ansible.builtin.service:
        name: charlie
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:44Z
